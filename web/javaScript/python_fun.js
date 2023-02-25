async function info_audio(){
                let url = document.getElementById('url').value;

                let result = await eel.view_url(url)();

                document.getElementById('info').innerHTML = result;

            }



async function download_video_js(){
            let url = document.getElementById('url').value;

            let result = await eel.download_video(url)();

            document.getElementById('download').innerHTML = result;
        }



async function download_audio_js(){
            let url = document.getElementById('url').value;

            let result = await eel.download_audio(url)();

            document.getElementById('download').innerHTML = result;
        }


async function search_clearing_js(){
            let url = document.getElementById('url').value;
            document.getElementById('url').value = '';
        }

document.getElementById("search_url").onclick = info_audio;
document.getElementById("search_clearing").onclick = search_clearing_js;
document.getElementById("download_audio_file").onclick = download_audio_js;
document.getElementById("download_video_file").onclick = download_video_js;

