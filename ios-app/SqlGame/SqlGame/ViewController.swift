import UIKit
import WebKit

class ViewController: UIViewController, WKNavigationDelegate, WKUIDelegate {
    
    private var webView: WKWebView!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupWebView()
        loadSqlGame()
    }

    private func setupWebView() {
        let webConfiguration = WKWebViewConfiguration()
        
        // 启用JavaScript
        webConfiguration.preferences.javaScriptEnabled = true
        
        // 启用DOM存储
        webConfiguration.websiteDataStore = WKWebsiteDataStore.default()
        
        // 创建WebView
        webView = WKWebView(frame: view.bounds, configuration: webConfiguration)
        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        
        // 添加到视图
        view.addSubview(webView)
    }

    private func loadSqlGame() {
        // 加载本地HTML文件
        if let htmlPath = Bundle.main.path(forResource: "index", ofType: "html") {
            let htmlURL = URL(fileURLWithPath: htmlPath)
            webView.loadFileURL(htmlURL, allowingReadAccessTo: htmlURL.deletingLastPathComponent())
        }
    }

    // 处理返回按钮
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        navigationController?.setNavigationBarHidden(true, animated: animated)
    }

    // WKNavigationDelegate方法
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        print("WebView loaded successfully")
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        print("WebView load failed: \(error.localizedDescription)")
    }

    // 处理JavaScript弹窗
    func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = UIAlertController(title: "提示", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "确定", style: .default, handler: { _ in
            completionHandler()
        }))
        present(alert, animated: true, completion: nil)
    }

    // 处理返回手势
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        navigationController?.setNavigationBarHidden(false, animated: animated)
    }

    // 支持返回按钮
    override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
        return false
    }
}
