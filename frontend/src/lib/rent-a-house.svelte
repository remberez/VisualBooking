<script>
    import houseInForest from '../assets/popular-img/rent-a-house.png';
</script>

<main>
    <section>
        <img src="{houseInForest}" alt="">

        <div class="block">

            <div class="block3">
                <h1>Сдать жилье на VisualBooking</h1>
                <p>Получай доход, сдавай жилье.</p>                
            </div>

            <div class="block2">
               <a href="">
                <button>
                    Подробнее
                </button>
                    
                </a> 
            </div>
            
        </div>
    </section>
    
</main>

<style>

    button{
        text-decoration: none;
        color: white;
        border: none;
        width: 400px;
        height: 50px;
        font-size: 30px;
        border-radius: 10px;
        box-shadow: 4px 3px 5px black;
        background-color: var(--color);
    }

    .block3{
        text-align: end;
    }

    .block h1{
        font-weight: 500;
        font-size: 2vw;
    }

    .block p{
        font-size: 1.5vw;
        font-weight: 300;
        padding: 10px 0 10px 0;
    }

    .block2{
        margin-top: 40px;
        transition: all 0.3s ease 0s;
    }

    .block2:hover{
        transform: scale(1.1);
    }

    .block a{

    }

    .block{
        display: flex;
        justify-content: center;
        align-items: end;
        flex-direction: column;
        height: 600px;
        top: 0;
        right: 0;
        position: absolute;
        color: white;
        width: 700px;
        margin-right: 100px;
    }

    section{
        position: relative;
    }

    img{
        width: clamp(320px, 75.9vw, 1700px);
        height: 600px;
        object-fit: cover;
        border-radius: 50px;
    }

    main{       
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }
</style>