<script lang="ts">
  import Navbar from "$lib/components/navbar.svelte";
  import { onMount } from "svelte";
  import {
    fetchInfo,
    fetchURL,
  } from "$lib/components/functions/fetch-info.svelte";
  import type { Publication } from "$lib/components/types/publication.svelte";
  import { createPublication } from "$lib/components/types/publication.svelte";
  import BlogCard from "$lib/components/blog-card.svelte";

  let filterName: string = "";
  let selectedUsers: Array<any> = [];
  let url = "http://localhost:5000/api/get-info/";

  let users: Array<any> = [];
  let publications: Array<any> = [];
  let publicationsForCard: Array<Publication> = [];
  let selectedPublications: Array<Publication> = [];

  onMount(async () => {
    users = await fetchInfo(`${url}users`);
    for (let user of users) {
      let avatar = await fetchURL(
        `${url}user/avatar?username=${user.username}`,
        "/images/default-avatar.png",
      );
      user.avatar = avatar;
    }
    selectedUsers = users;
    publications = await fetchInfo(`${url}publications/latest`);
    for (let publication of publications) {
      publication.blob = await fetchURL(
        `${url}publication-thumbnail?id=${publication.id}`,
        "/images/default-publication.png",
      );
      publicationsForCard.push(
        createPublication(
          publication.id,
          publication.date,
          publication.title,
          publication.pub_type,
          publication.short_desc,
          publication.desc,
          publication.blob,
          publication.username,
          publication.avatar,
        ),
      );
      selectedPublications = publicationsForCard;
    }
  });

  function handleFilterChange() {
    if (filterName.trim() === "") {
      selectedUsers = users;
    } else {
      selectedUsers = users
        .filter((user) => {
          return user.username.toLowerCase().includes(filterName.toLowerCase());
        })
        .slice(0, 9);
    }
    console.log(publicationsForCard.length);
  }
</script>

<Navbar />
<div class="content">
  <section class="find-users px-5">
    <div class="container user-list p-3 px-5">
      <div class="row">
        <div class="col text-center mt-5 pb-5">
          <h2 class="text title mb-3 mt-2">Find Users</h2>
          <div class="filter-input neo-ov mb-4 mt-3">
            <div class="row d-flex justify-content-between text-center">
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

          {#if filterName}
            {#if selectedUsers.length > 0}
              <div
                class="row row-cols-3 row-cols-sm-3 row-cols-lg-3 row-cols-md-3 d-flex justify-content-between"
              >
                {#each selectedUsers as user}
                  <a href="/user/{user.username}" class="col-sm-3 mt-3 p-2">
                    <div class="neo-ov py-2">
                      <img
                        src={user.avatar}
                        alt=""
                        class="img-fluid rounded-circle"
                      />
                      <span class="text">{user.username}</span>
                    </div>
                  </a>
                {/each}
              </div>
            {:else}
              <div class="text-center">
                <h2 class="text title">No Users</h2>
              </div>
            {/if}
          {:else}
            <div class="text-center">
              <h2 class="text subtle">Try to search</h2>
            </div>
          {/if}
        </div>
      </div>
    </div>
  </section>
  <section>
    <div class="container latest-publications py-4 px-5">
      <div class="col text-center px-5">
        <h1 class="text title mt-5 mb-5">Latest Publications</h1>
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
  </section>
</div>

<style>
  ::placeholder {
    color: var(--muted);
  }

  input {
    color: var(--text);
    background-color: var(--base);
    transition: filter 0.3s ease;
    max-height: 2em;
  }

  input:hover,
  input:focus {
    filter: brightness(1.05);
    background-color: var(--base);
    color: var(--text);
  }

  a {
    text-decoration: none;
  }

  .neo-ov {
    transition: background-color 0.3s ease;
  }

  .neo-ov:hover {
    background-color: var(--base);
  }

  .filter-input {
    padding: 1em;
    border-radius: 15px;
  }

  .user-list,
  .latest-publications {
    background-color: var(--panel);
    border-radius: 20px;
  }
  .find-users img {
    height: 5em;
    width: 5em;
  }

  .latest-publications {
    margin-top: 5%;
  }

  .content {
    background: url("/images/explore-bg.jpg");
    background-size: cover;
    padding: 10% 0 5% 0;
  }
</style>
