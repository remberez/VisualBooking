<script>
    export let hrefs = "https://avatars.mds.yandex.net/i?id=2a4caaaacef0bd85c8d7a4676f0a6ed4_l-4079525-images-thumbs&n=13"
    export let name = "Новый крутdой дом"
    export let time = 50


    let line;
    let intervalId;

    function effect() {
        line.style.display = "block"; 
    }

    function reset() {
        clearInterval(intervalId);
        line.style.display = "none";
    }
</script>

<main on:mouseenter={effect} on:mouseleave={reset}>
    <section>
        <img src={hrefs} alt="">

        <p id="time">{time} мин</p>
    </section>
    
    <p id="name-news">{name}</p>
    <br>
    <hr bind:this={line}>
    <br>
</main>

<style>

    hr{
        width: clamp(300px,20.8333vw,300px); 
        height: 4px;
        background-color: rgba(126, 126, 126, 0.692);
        border: none;
        border-radius: 10px;
        opacity: 0;animation: ani 0.4s forwards;
        display: none;
    }

    @keyframes ani {
    0% {opacity: 0;}
    100% {opacity: 1;}
    }

    main{
        width: clamp(300px,20.8333vw,300px); 
        transition: all 0.3s ease 0s;
    }

    #name-news{
        font-size: 30px;
        padding-top: 20px;
        text-align: center;
    }

    img{
      max-width: 100%; 
      height: auto;    
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 10px; 
    }

    #time{
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: white;
        padding: 2px;
        border-radius: 10px;
        margin: 0 10px 10px 0;
    }

    section{
        width: clamp(300px,20.8333vw,300px); 
        position: relative;
    }
</style>