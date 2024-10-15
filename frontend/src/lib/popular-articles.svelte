<script>
    import NewsBlock from "./news-block.svelte";
</script>

<main>
    <h1>Популярные статьи</h1>

    <section>
        <NewsBlock hrefs="https://www.wikihow.com/images/thumb/a/a2/Include-CSS-Within-HTML-Web-Pages-Step-6.jpg/aid4377690-v4-728px-Include-CSS-Within-HTML-Web-Pages-Step-6.jpg.webp"/>
        <NewsBlock/>
        <NewsBlock/>
        <NewsBlock/>
    </section>

    <div class="block">
        <div class="block2">
            <a id="podrobno" href="">Читать больше</a>            
        </div>

    </div>
</main>

<style>
    #podrobno{
        background-color: var(--color);
        padding: 10px 20px 10px 20px;
        color: white;
        text-decoration: none;
        border-radius: 10px;
        font-size: clamp(19px,1.4vw,25px);
        box-shadow: 4px 3px 7px black;
        text-align: start;
        margin-left: 20px;
    }

    .block2:hover{
        transform: scale(1.1);
    }
    .block2{
        transition: all 0.3s ease 0s;
        width: 300px;
    }

    .block{
        margin-top: 20px;
        width: clamp(320px,100%,1300px);
    }

    h1{
        font-size: clamp(40px,2.6vw,60px);
        text-align: center;
    }

    section{
        margin-top: 60px;
        width: clamp(320px,100%,1300px);
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-wrap: wrap;
    }

    main{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 0 auto;
        width: clamp(320px,100%,1500px);
        box-shadow: 0 0 3px red;
        padding: 100px 0 100px 0;
    }
</style>