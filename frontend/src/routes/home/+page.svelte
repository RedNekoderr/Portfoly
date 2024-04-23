<script lang="ts">
  import Navbar from "$lib/components/navbar.svelte";
  import ArrowRight from "svelte-bootstrap-icons/lib/ArrowRight.svelte";
  import { t } from "$lib/translate.svelte";
</script>

<Navbar />

<header class="">
  <div class="row">
    <div class="col text-center">
      <h1 class="text title">{$t("home.title")}</h1>
      <p class="text subtle">{$t("home.title.subtitle")}</p>
    </div>
    <div class="row">
      <div class="col d-flex justify-content-end">
        <a href="/profile" class="button get-started-btn"
          >{$t("home.title.button.getStarted")}</a
        >
      </div>
      <div class="col d-flex justify-content-start">
        <a href="/home#about" class="button"
          >{$t("home.title.button.learnMore")} <ArrowRight /></a
        >
      </div>
    </div>
  </div>
</header>
<div class="container mt-5">
  <div class="row">
    <div class="col text-center">
      <h1 class="text title">{$t("home.features.title")}</h1>
    </div>
  </div>
</div>

<style lang="scss">
  header {
    padding: 15% 0;
    background-color: #adb7f2;
    background: url(images/header-bg.jpg);
    border-radius: 0 0 5% 5%;
    position: relative;
    border: none;
    overflow: hidden;
  }
  .get-started-btn {
    background: var(--foam);
    color: var(--overlay);
  }
</style>
