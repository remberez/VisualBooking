<script>
  import Header from './lib/Header.svelte'
  import MainPhoto from './lib/MainPhoto.svelte'
  import Popular from './lib/popular.svelte'
  import SocialNetwork from './lib/social-network.svelte'
  import PopularObject from './lib/popular-object.svelte'
  import PopularArticles from './lib/popular-articles.svelte'
  import RentAHouse from './lib/rent-a-house.svelte'
  import Footer from './lib/footer.svelte'

  import axios from 'axios';
     let bannerData = null; 

     axios.get('https://fortnite-api.com/v1/banners')
       .then(response => {
         bannerData = response.data.status ;
       })
       .catch(error => {
         console.error('Ошибка при получении данных:', error);
       });
</script>

<main>
  <Header/>
  <MainPhoto/>
  <Popular/>
  <SocialNetwork/>
  <PopularObject/>
  <PopularArticles/>
  <RentAHouse/>
  <Footer/>
  <br>
  <br>  <br>  <br>  <br>  <br>  <br>
  {#if bannerData}
    <p>Данные: {bannerData.someProperty}</p>
  {/if}
  <br>
  <br>  <br>  <br>  <br>  <br>  <br>
</main>

<style>

</style>
