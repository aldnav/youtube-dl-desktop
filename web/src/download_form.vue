<template>
    <aside id="main">
        <div class="outer">
        <div class="container">
            <h1>DOWNLOAD VIDEOS FROM YOUTUBE</h1>
            <form v-on:submit="download">
                <div class="formset">
                    <label for="url">PASTE LINK HERE</label>
                    <input type="text" id="url" name="url" placeholder="e.g. https://www.youtube.com/watch?v=vmGlQSACCIA" v-model="url">
                </div>
                <button>DOWNLOAD</button>
            </form>
        </div>
        </div>
    </aside>
</template>

<script>
import { eventBus } from './main';

export default {
    name: 'downloadForm',
    data() {
        return {'url': ''};
    },
    methods: {
        download(event) {
            event.preventDefault();
            let downloadUrl = this.url.trim()
            if (!downloadUrl) {
                return;
            }
            this.url = '';
            eel.queue_download(downloadUrl)().then(data => {
                eventBus.addDownload(data);
            });
        }
    }
}
</script>

<style lang="scss" scoped>

#main {
    height: 80%;
    width: 60%;
    display: inline-block;

    .outer {
        display: flex;
        height: 100%;
    }
}

.container {
    margin: auto;
}

h1 {
    color: #ffffff;
    font-family: "NotoSans";
    font-weight: bold;
    font-size: 22px;
}

.formset {
    background-color: #232323;
    padding: 15px 20px;
    border-radius: 3px;
    border: 0.5px solid #4c4c4c;
    text-align: left;
    vertical-align: middle;
    margin-top: 40px;

    label {
        color: #6d6d6d;
        font-family: "NotoSans";
        text-align: left;
        font-size: 14px;
        line-height: 23px;
        vertical-align: top;
        font-weight: bold;
    }

    input {
        background-color: #232323;
        border: none;
        color: #6d6d6d;
        width: 300px;
        margin-left: 20px;
        font-style: italic;
        font-size: 12px;
        padding: 5px;
    }
}

button {
    margin-top: 30px;
    background-color: #ff0000;
    border: none;
    border-radius: 3px;
    color: #ffffff;
    font-weight: bold;
    font-size: 17px;
    padding: 15px 30px;
    font-family: "NotoSans";

}

</style>