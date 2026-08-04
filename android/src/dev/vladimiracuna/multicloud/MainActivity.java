package dev.vladimiracuna.multicloud;

import android.app.Activity;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.ViewGroup;
import android.webkit.ServiceWorkerClient;
import android.webkit.ServiceWorkerController;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

/**
 * El programa completo empaquetado: las 288 clases viajan en los assets, asi que
 * la aplicacion funciona sin conexion.
 *
 * <p>Los assets NO se cargan con file:// sino a traves de un origen https
 * virtual servido desde {@link #shouldInterceptRequest}. La razon es concreta:
 * con file:// el portal no puede hacer fetch("catalog.json") —origen opaco— y
 * la pantalla queda en blanco. Con un origen https propio, fetch, localStorage
 * y el progreso guardado funcionan igual que en el portal web.
 */
public class MainActivity extends Activity {

  private static final String ORIGIN = "https://appassets.androidplatform.net";
  private static final String HOME = ORIGIN + "/site/index.html";
  private static final String HOST = "appassets.androidplatform.net";

  private static final Map<String, String> MIME_TYPES = new HashMap<>();

  static {
    MIME_TYPES.put("html", "text/html");
    MIME_TYPES.put("js", "text/javascript");
    MIME_TYPES.put("mjs", "text/javascript");
    MIME_TYPES.put("css", "text/css");
    MIME_TYPES.put("json", "application/json");
    MIME_TYPES.put("webmanifest", "application/manifest+json");
    MIME_TYPES.put("svg", "image/svg+xml");
    MIME_TYPES.put("png", "image/png");
    MIME_TYPES.put("jpg", "image/jpeg");
    MIME_TYPES.put("jpeg", "image/jpeg");
    MIME_TYPES.put("webp", "image/webp");
    MIME_TYPES.put("ico", "image/x-icon");
    MIME_TYPES.put("woff2", "font/woff2");
    MIME_TYPES.put("xml", "application/xml");
    MIME_TYPES.put("txt", "text/plain");
    MIME_TYPES.put("pdf", "application/pdf");
  }

  private WebView webView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    FrameLayout root = new FrameLayout(this);
    root.setBackgroundColor(Color.parseColor("#111713"));
    root.setLayoutParams(new ViewGroup.LayoutParams(
        ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

    webView = new WebView(this);
    webView.setBackgroundColor(Color.parseColor("#111713"));
    webView.setLayoutParams(new ViewGroup.LayoutParams(
        ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

    WebSettings settings = webView.getSettings();
    settings.setJavaScriptEnabled(true);
    settings.setDomStorageEnabled(true);
    settings.setAllowFileAccess(false);
    settings.setAllowContentAccess(false);
    settings.setSupportZoom(true);
    settings.setBuiltInZoomControls(true);
    settings.setDisplayZoomControls(false);
    settings.setMediaPlaybackRequiresUserGesture(true);
    settings.setCacheMode(WebSettings.LOAD_DEFAULT);

    webView.setWebViewClient(new WebViewClient() {
      @Override
      public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
        return openExternally(request.getUrl());
      }

      @Override
      public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
        return serveAsset(request.getUrl());
      }
    });

    // El portal registra su service worker en cualquier origen https. Si sus
    // peticiones no se interceptan tambien aqui, saldrian a la red real y la
    // instalacion fallaria; con esto se sirven de los mismos assets.
    ServiceWorkerController.getInstance().setServiceWorkerClient(new ServiceWorkerClient() {
      @Override
      public WebResourceResponse shouldInterceptRequest(WebResourceRequest request) {
        return serveAsset(request.getUrl());
      }
    });

    root.addView(webView);
    setContentView(root);

    if (savedInstanceState != null) {
      webView.restoreState(savedInstanceState);
    } else {
      webView.loadUrl(HOME);
    }
  }

  /** Sirve el curso empaquetado; devuelve null para que el resto siga su curso. */
  private WebResourceResponse serveAsset(Uri uri) {
    if (uri == null || !HOST.equals(uri.getHost())) {
      return null;
    }
    String path = uri.getPath();
    if (path == null || path.isEmpty() || path.equals("/")) {
      path = "/site/index.html";
    }
    // El portal precachea "./", que llega como directorio: se sirve su indice.
    if (path.endsWith("/")) {
      path = path + "index.html";
    }
    // Ni rutas relativas ni escapes fuera de los assets.
    if (path.contains("..")) {
      return forbidden();
    }
    String assetPath = path.substring(1);
    AssetManager assets = getAssets();
    try {
      InputStream stream = assets.open(assetPath);
      WebResourceResponse response =
          new WebResourceResponse(mimeType(assetPath), "utf-8", stream);
      response.setStatusCodeAndReasonPhrase(200, "OK");
      response.setResponseHeaders(Collections.singletonMap("Cache-Control", "no-cache"));
      return response;
    } catch (IOException notFound) {
      WebResourceResponse response = new WebResourceResponse(
          "text/plain", "utf-8",
          new ByteArrayInputStream(("404 " + assetPath).getBytes(StandardCharsets.UTF_8)));
      response.setStatusCodeAndReasonPhrase(404, "Not Found");
      return response;
    }
  }

  private WebResourceResponse forbidden() {
    WebResourceResponse response = new WebResourceResponse(
        "text/plain", "utf-8", new ByteArrayInputStream("403".getBytes(StandardCharsets.UTF_8)));
    response.setStatusCodeAndReasonPhrase(403, "Forbidden");
    return response;
  }

  private static String mimeType(String path) {
    int dot = path.lastIndexOf('.');
    if (dot < 0) {
      return "application/octet-stream";
    }
    String extension = path.substring(dot + 1).toLowerCase(Locale.ROOT);
    String mime = MIME_TYPES.get(extension);
    return mime == null ? "application/octet-stream" : mime;
  }

  /** Todo lo que no sea el curso empaquetado se abre fuera de la aplicacion. */
  private boolean openExternally(Uri uri) {
    if (uri != null && HOST.equals(uri.getHost())) {
      return false;
    }
    String scheme = uri == null ? null : uri.getScheme();
    if (!"http".equals(scheme) && !"https".equals(scheme) && !"mailto".equals(scheme)) {
      return true;
    }
    try {
      Intent intent = new Intent(Intent.ACTION_VIEW, uri);
      intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
      startActivity(intent);
    } catch (RuntimeException ignored) {
      // Sin aplicacion capaz de abrirlo: se ignora en vez de romper la navegacion.
    }
    return true;
  }

  @Override
  public boolean onKeyDown(int keyCode, KeyEvent event) {
    if (keyCode == KeyEvent.KEYCODE_BACK && webView != null && webView.canGoBack()) {
      webView.goBack();
      return true;
    }
    return super.onKeyDown(keyCode, event);
  }

  @Override
  protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);
    if (webView != null) {
      webView.saveState(outState);
    }
  }
}
