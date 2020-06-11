const { app, BrowserWindow } = require('electron')

function createWindow() {
    // Create the browser window.
    let win = new BrowserWindow({
        show: false,
        width: 1600,
        height: 900,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.maximize();
    win.show();

    // Load the index.html of the app.
    win.loadFile('index.html')

    win.webContents.openDevTools()
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})