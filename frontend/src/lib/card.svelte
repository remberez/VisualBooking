<script>
    export let nameChapter = "Гостевой дом "
    export let nameObject = "Вавилон"
    export let city = "Cаратов"
    export let distans = 32
    export let hrefs = "https://cache3.youla.io/files/images/780_780/5a/f3/5af3c7c9f8efdc8b0e3020b9.jpg"
    export let sale = 1904
</script>

<main>
    <a href="">
        <img src="{hrefs}" alt="">

        <p id="one">{nameChapter} "{nameObject}"</p>
        <p id="two">{city}, {distans}км</p>
        <br>
        <br>
        <p id="sale">от {sale} руб <span>в сутки</span></p>
    </a>
    
</main>

<style>
    span{
        font-size: 15px;
        color: gray;
    }

    #sale{
        font-size: 25px;
    }

    #one{
        font-size: 18px;
    }

    #two{
        color: gray;
        font-size: 15px;
    }

    main{
        display: flex;
        justify-content: center;
        align-items: center;
    }

    img{
        width: 300px;
        padding: 10px;
        border-radius: 10px;
    }

    a{
        text-decoration: none;
        color: black;
    }
</style>