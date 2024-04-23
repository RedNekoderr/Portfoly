<script lang="ts">
  import { getCookie } from "./functions/cookies.svelte";
  import { onMount } from "svelte";

  import { fetchURL, fetchInfo } from "./functions/fetch-info.svelte";
  import { getPublications } from "./functions/fetch-publications.svelte";
  import BlogCard from "./blog-card.svelte";
  import {
    ArrowRightCircle,
    Person,
    TextParagraph,
  } from "svelte-bootstrap-icons";
  import { isContentChanged } from "$lib/store.svelte";

  let filterType: string = "all";
  let filterName: string = "";

  let fetch_url = `http://localhost:5000/api/get-info/`;
  let defaultAvatarUrl: string = "images/default-avatar.png";
  let defaultBannerUrl: string = "images/default-banner.jpg";

  let avatarUrl: string;
  let bannerUrl: string;

  export let username: string = "";
  export let isProfilePage: boolean = false;
  let publications: Array<any> = [];
  export let selectedPublications: Array<any> = [];

  let userDescription: string;

  function updateSelectedPublication() {
    selectedPublications = publications;
  }

  function handleFilterChange() {
    filterPublications();
  }

  function filterPublications() {
    selectedPublications = publications.filter((publication) => {
      if (filterType === "all" || publication.pubType === filterType) {
        return (
          publication.title.toLowerCase().includes(filterName.toLowerCase()) ||
          publication.shortDesc.toLowerCase().includes(filterName.toLowerCase())
        );
      }
      return false;
    });
  }

  export const updateInfoOnContentChange = async () => {
    console.log($isContentChanged);
    if ($isContentChanged) {
      updateInfo();
      isContentChanged.set(false);
    }
  };

  let updateInfo = async () => {
    publications = await getPublications(username);
    let fetch_avatar_url = `${fetch_url}user/avatar?username=${username}`;
    let fetch_banner_url = `${fetch_url}user/banner?username=${username}`;

    avatarUrl = await fetchURL(fetch_avatar_url, defaultAvatarUrl);
    bannerUrl = await fetchURL(fetch_banner_url, defaultBannerUrl);
    updateSelectedPublication();

    userDescription = await fetchInfo(
      `${fetch_url}user/description?username=${username}`,
    ).then((response) => response.desc);
  };

  onMount(async () => {
    if (isProfilePage) {
      username = getCookie("username");
    }
    updateInfo();
  });

  $: {
    filterPublications();
  }
</script>

{#if bannerUrl}
  <div
    class="banner"
    style="background-image: url({bannerUrl}); background-repeat: no-repeat; background-size: cover;"
  />
{/if}
<section class="vw-100">
  <div class="container-fluid main-content">
    <div class="container">
      <div class="row d-flex justify-content-around">
        <div class="col-sm-3 mt-5 neo-hl text-center py-2">
          {#if avatarUrl}
            <img
              src={avatarUrl}
              alt="User Avatar"
              class="avatar rounded-circle"
            />
          {/if}
        </div>

        <div class="col-sm-8 mt-5">
          <div class="neo-hl h-100 px-5 py-2">
            <h1 class="username coolvetica d-flex align-items-center">
              <Person width={48} height={48} />{username}
            </h1>
            <p class="subtle">
              <TextParagraph width={24} height={24} />
              {userDescription}
              <a href="/profile#uploads" class="btn btn-sm desc-button">
                <ArrowRightCircle />
              </a>
            </p>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col text-center mt-5 pb-5">
          <h2 class="text title mb-3 mt-2" id="uploads">Uploads</h2>
          <div class="filter-input neo-ov mb-4 mt-3">
            <div class="row d-flex justify-content-between text-center">
              <div class="col">
                <select
                  bind:value={filterType}
                  class="form-select"
                  on:change={handleFilterChange}
                >
                  <option value="all">All</option>
                  <option value="it">IT</option>
                  <option value="art">Art</option>
                  <option value="article">Article</option>
                </select>
              </div>
              <div class="col">
                <input
                  bind:value={filterName}
                  type="text"
                  class="form-control"
                  placeholder="Search"
                  on:input={handleFilterChange}
                />
              </div>
            </div>
          </div>
          {#if selectedPublications.length > 0}
            <div
              class="row row-cols-md-2 row-cols-lg-2 d-flex justify-content-between"
            >
              {#each selectedPublications as publication}
                <BlogCard {publication} />
              {/each}
            </div>
          {:else}
            <div class="text-center">
              <h2 class="text title">No publications</h2>
            </div>
          {/if}
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  section {
    padding: 320px 0 0 0;
  }

  ::placeholder {
    color: var(--muted);
  }

  select {
    padding: 0;
    padding: 0.3rem 0.75rem 0 0.75rem;
  }

  select,
  input {
    color: var(--text);
    background-color: var(--base);
    transition: filter 0.3s ease;
    max-height: 2em;
  }

  select:hover,
  select:focus,
  input:hover,
  input:focus {
    filter: brightness(1.05);
    background-color: var(--base);
    color: var(--text);
  }

  .banner {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
  }

  .desc-button {
    border: none;
    background: none;
    padding: 0;
    margin: 0;
    translate: 0 -4px;
  }

  .main-content {
    background-color: var(--base);
    border-radius: 100px 100px 0 0;
  }

  .username {
    font-size: 3.8em;
    margin: auto 0;
  }

  .filter-input {
    padding: 1em;
    border-radius: 15px;
  }

  @media only screen and (max-width: 1200px) {
    .avatar {
      width: 100px;
    }
  }

  @media only screen and (min-width: 1200px) {
    .avatar {
      width: 225px;
      height: 225px;
      border: 5px solid var(--highlight-high);
    }
  }
</style>
