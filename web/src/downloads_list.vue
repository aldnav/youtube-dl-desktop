<template>
    <aside id="downloads">
        <span class="heading">
            <h3>DOWNLOADS</h3>
        </span>
        <div class="download-items">
            <div class="item" v-for="download in downloads">
                <img v-bind:src="download.image_url" alt="preview-image">
                <div class="details">
                    <h4>{{ download.title }}</h4>
                    <div class="progress-bar" v-if="download.status === 'downloading'">
                        <div class="progress" v-bind:style="'width: ' + download.downloadInfo._percent_str"></div>
                    </div>
                    <p v-if="download.status === 'downloading'">{{ download.downloadInfo._speed_str }} - {{ toMB(download.downloadInfo.downloaded_bytes) }} / {{ toMB(download.downloadInfo.total_bytes) }} MB, {{ download.downloadInfo._eta_str }} left</p>
                    <p v-if="download.status != 'downloading'">{{ download.status }}</p>
                </div>
            </div>
        </div>
    </aside>
</template>

<script>
import { eventBus } from './main';


export default {
    data() {
        return {
            downloads: []
        }
    },

    methods: {
        toMB(bytes) {
            return Math.round(bytes / 1000000 * 100) / 100
        }
    },

    created() {
        eel.list_downloads()().then(data => {
            this.downloads = data.reverse();
        });
        eventBus.$on('addDownload', download => {
            this.downloads.unshift(download);
        });

        window.addEventListener('updateDownload', e => {
            let updatedDl = e.detail;
            let existing = this.downloads.find(obj => {
                return obj.key === updatedDl.key;
            });
            existing.downloadInfo = updatedDl.downloadInfo;
            existing.status = updatedDl.status;
        });
    }
}
</script>

<style lang="scss" scoped>

#downloads {
    width: 35%;
    display: inline-block;
    vertical-align: top;
    text-align: left;
    height: 100%;
    overflow-y: scroll;
    background-color: #2b2b2b;
    float:right;

    h3 {
        color: #6d6d6d;
        font-family: "NotoSans";
        margin-left: 30px;
        font-size: 20px;
    }

    .item {
        display: block;
        padding: 10px;
        padding-left: 30px;

        img {
            display: inline-block;
            width: 30%;
            max-width: 130px;
        }

        .details {
            display: inline-block;
            width: 65%;
            vertical-align: top;
            padding-left: 10px;

            h4 {
                margin: 0px;
                color: #ffffff;
                text-overflow: ellipsis;
                white-space: nowrap;
                overflow:hidden;
            }

            .progress-bar {
                background-color: #343434;
                width: 60%;
                height: 10px;
                border-radius: 3px;
                margin-top: 8px;

                .progress {
                    background-color: #ff0000;
                    height: 100%;
                    border-radius: 3px;
                }
            }

            p {
                margin: 0px;
                margin-top: 6px;
                color: #6d6d6d;
                font-family: "NotoSans";
                font-size: 13px;
            }
        }
    }

    .item:hover {
        background-color: #121212;
    }
}

</style>