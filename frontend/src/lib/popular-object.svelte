<script>
import Card from "./card.svelte";

let activeButton = null;

function setActive(buttonNumber) {
    if (activeButton !== buttonNumber)  activeButton = buttonNumber;
}

</script>

<main>
    <h1>Объекты с лучшим рейтингом</h1>

    <section>
        <button class={activeButton === 1 ? 'active' : ''} on:click={() => setActive(1)} id="b1">Гостевые дома</button>
        <hr id="vertical-line">
        <button class={activeButton === 2 ? 'active' : ''} on:click={() => setActive(2)} id="b2">Частный сектор</button>
        <hr id="vertical-line">
        <button class={activeButton === 3 ? 'active' : ''} on:click={() => setActive(3)} id="b3">Базы отдыха</button>
        <hr id="vertical-line">
        <button class={activeButton === 4 ? 'active' : ''} on:click={() => setActive(4)} id="b4">Квартиры посуточно</button>
    </section>

    <hr id="gorizontal-line">

    <nav>
        <Card/>
        <Card/>
        <Card/>
        <Card/>
        <Card/>
        <Card/>
        <Card/>
        <Card/>
    </nav>

    <div class="block">
        <a id="more-variants" href="">Смотреть еще 120 вариантов</a>
    </div>
    <br>    <br>    
</main>

<style>
    nav{
        margin-top: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: clamp(320px,100%,1500px);
        flex-wrap: wrap;
        gap: 20px;
    }

    #more-variants{
        background-color: var(--color);
        padding: 10px 20px 10px 20px;
        color: white;
        text-decoration: none;
        border-radius: 10px;
        font-size: clamp(19px,1.4vw,25px);
        box-shadow: 4px 3px 7px black;
    }

    .block{
        margin-top: 100px;
        /* box-shadow: 0 0 3px red; */
        text-align: end;
        width: clamp(320px,100%,1300px);
    }

    #vertical-line{
        transform: rotate(-90deg);
        width: 50px;
  
    }

    .active {
        background-color: var(--color);
        color: white;
        transform: scale(1.1);
        padding: 10px 25px 10px 25px;
    }

    #gorizontal-line{
        width: 100%;
        display: none;
        margin-top: 50px;
    }

    main{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 0 auto;
        width: clamp(320px,100%,1500px);
        /* box-shadow: 0 0 3px red; */
        padding-top: 100px;
    }

    h1{
        font-size: clamp(40px,2.6vw,60px);
        text-align: center;
    }

    button{
        font-size: clamp(30px,1.8vw,30px);
        padding: 10px;
        background-color: transparent;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease 0s;
    }

    section{
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        width: 100%;
        margin-top: 30px;
        flex-wrap: wrap;
        gap: 20px;
    }

    @media(max-width:725px){
        section{
            flex-wrap: wrap;
            flex: 1 1;
        }

        #gorizontal-line{
            display: block;
        }

    }

    @media(max-width:1290px){
        #vertical-line{
            display: none;
        }
    }

    
    @media(max-width:933px){
        .block{
            text-align: center;
        }
    }
</style>