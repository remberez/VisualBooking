<script>
    import src1 from "../assets/popular-img/1.png";
    import src2 from "../assets/popular-img/2.png";
    import src3 from "../assets/popular-img/3.png";
    import blur from '../assets/blur-popular.png';
</script>

<main>
    <h1>Популярное</h1>

    <section>
        <div class="photo">
            <img src="{src1}" alt="">
            <img id="blur" src="{blur}" alt="">
            <h2>Геленджик</h2>
        </div>

        <div class="photo">
            <img src="{src2}" alt="">
            <img id="blur" src="{blur}" alt="">
            <h2>Кабардинка</h2>
        </div>

        <div class="photo">
            <img src="{src3}" alt="">
            <img id="blur" src="{blur}" alt="">
            <h2>Дивноморское</h2>
        </div>
    </section>
</main>

<style>
    main {
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      margin-top: 10px;
    }

    section{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 30px;
        margin-top: 20px;
    }

    .photo:hover{
        transform: scale(1.1);
    }
    main h1 {
      font-size: clamp(40px,2.6vw,60px);
    }

    .photo {
      position: relative;
      width: clamp(300px,20.8333vw,400px); 
      transition: all 0.3s ease 0s;
    }

    .photo img {
      max-width: 100%; 
      height: auto;    
      width: 100%;
      height: 100%;
      object-fit: cover; 
    }

    #blur {
      position: absolute;
      top: 0;
      left: 0; 
      z-index: 1; 
    }

    h2 {
      position: absolute;
      bottom: 10px; 
      left: 50%; 
      transform: translateX(-50%); 
      z-index: 2;
      color: white; 
      text-align: center; 
    }

    @media(max-width:928px)
    {
      section{
        flex-direction: column;
        justify-content: center;
      }
    }
  </style>