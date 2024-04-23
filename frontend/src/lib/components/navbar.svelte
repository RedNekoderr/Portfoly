<script lang="ts">
  import { locale, locales } from "$lib/translate.svelte";
</script>

<nav class="container justify-content-between fixed-panel">
  <div class="row">
    <div class="col text-start">
      <a href="/home" class="text button coolvetica">Home</a>
      <a href="/home#about" class="text button coolvetica">About</a>
    </div>
    <div class="col text-center">
      <a href="/user" class="text button coolvetica">Explore</a>
    </div>
    <div class="col text-end d-flex flex-row justify-content-end">
      <div class="select-wrap d-flex align-items-center">
        <select bind:value={$locale} class="text coolvetica subtle">
          {#each locales as l}
            <option value={l}>{l}</option>
          {/each}
        </select>
      </div>

      <a href="/profile" class="text button coolvetica">Profile</a>
    </div>
  </div>
</nav>

<style>
  select {
    border-radius: 5px;
    transition: background-color 0.2s ease;
  }

  ::placeholder {
    color: var(--muted);
  }

  select,
  ::file-selector-button {
    color: var(--text);
  }

  select,
  select:focus,
  ::file-selector-button {
    background-color: transparent;
  }

  select:hover {
    background-color: var(--highlight-low);
  }

  a,
  select {
    line-height: 1;
  }

  .fixed-panel {
    position: fixed;
    top: 1%;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    max-width: 90vw;
    padding: 7px;
    border-radius: 10px;
    background-color: var(--panel);
    z-index: 1000;
    backdrop-filter: blur(10px);
  }

  .fixed-panel a {
    font-size: 1.4rem;
    margin: 0 5px;
  }
</style>
