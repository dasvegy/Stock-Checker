# Stock-Checker
A app which checks if the Item you want is in Stock or not, and then sends a Notification

## How it works
1. Download the Zip on the [releases](https://github.com/dasvegy/Stock-Checker/releases) page and unzip it.
2. Open the Folder and there should be a file called .env
3. Open the file. In the 'PRODUCT' section, you can type whatever you want. In the 'PHRASE' section, there should be a keyword that indicates the product is out of stock. In the 'URL' section, you put the URL of the product.
4. You could now open it and get a notification if the product is in stock. But it wouldnt be automated.

### Windows 
You can open "Task Sceduler" and Scedule a task that runs every hour or so.

### Linux
You can make a service using systemd.
