let app = {
    init: function() {
        this.activateForm();
        let func = this.listExistingDownloads
        let _this = this;
        setInterval(function() {
            _this.listExistingDownloads();
        }, 1000)
    },
    activateForm: function() {
        document.querySelector('form').addEventListener('submit', (e) => {
            e.preventDefault();
            let urlField = document.querySelector('#url');
            url = urlField.value.trim()
            urlField.value = ''
            if (url) {
                this.queueDownload(url);
            }
        });
    },
    listExistingDownloads: function() {
        eel.list_active_downloads()().then(items => {
            list.innerHTML = '';
            items.forEach(item => {
                this.addToQueueList(item);
            })
        });
    },
    queueDownload: function(url) {
        console.log('queueing');
        eel.queue_download(url)().then(data => {
            this.addToQueueList(data);
        });
    },
    addToQueueList: function(data) {
        let template = `<li data-key="${data.key}">${data.progress}% - ${data.url}</li>`;
        let list = document.querySelector('#list');
        list.innerHTML += template;
    }

}

app.init();