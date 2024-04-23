<script lang="ts">
  import { getCookie } from "../functions/cookies.svelte";
  import { getPublications } from "../functions/fetch-publications.svelte";
  import { onMount } from "svelte";
  import { createEventDispatcher } from "svelte";
  import { isContentChanged } from "$lib/store.svelte";
  import NewPubForm from "./new-pub-form.svelte";
  import EditPubForm from "./edit-pub-form.svelte";
  import UserBioForm from "./userBioForm.svelte";
  import UpdateImageForm from "./updateImageForm.svelte";
  import UserLogout from "./userLogout.svelte";
  import Sidemenu from "../sidemenu.svelte";
  import { createElement } from "../types/elementInfo.svelte";
  import { fetchURL, fetchInfo } from "../functions/fetch-info.svelte";
  import type { Publication } from "../types/publication.svelte";
  import type { Element } from "../types/elementInfo.svelte";

  const dispatch = createEventDispatcher();
  const sections: Array<Element> = [
    createElement("New", []),
    createElement("Edit", []),
    createElement("Bio", []),
    createElement("Avatar", []),
    createElement("Banner", []),
    createElement("Sign out", []),
  ];

  let username = getCookie("username");
  let avatar: any;
  let banner: any;
  let bio: any;
  let publications: Array<any>;
  let publicationElements: Array<Element>;

  let updateEditMenu: any;

  let selectedSection: string = "new";
  let selectedPublication: Publication;

  function updatePublicationElements(publications: Array<any>) {
    let publicationElements = [];
    for (let publication of publications) {
      publicationElements.push(
        createElement(publication.title, [publication.pubType]),
      );
    }
    return publicationElements;
  }

  function updateSelectedPublication(publication: any) {
    if (publication) {
      selectedPublication = publication;
    }
  }

  async function sendComponentUpdate(event: CustomEvent) {
    publications = await getPublications(username);
    publicationElements = updatePublicationElements(publications);
    if (typeof updateEditMenu === "function") {
      updateEditMenu(publicationElements, event.detail);
    }
    isContentChanged.set(true);
    dispatch("componentUpdate");
  }

  function handleMainMenuClick(event: CustomEvent) {
    selectedSection = event.detail;
    updateSelectedPublication(publications[0]);
  }

  function handleEditMenuClick(event: CustomEvent) {
    for (let publication of publications) {
      if (publication.title.toLowerCase() === event.detail.toLowerCase()) {
        updateSelectedPublication(publication);
        break;
      }
    }
  }

  onMount(async () => {
    publications = await getPublications(username);
    let url = "http://localhost:5000/api/get-info/user/";
    avatar = await fetchURL(
      `${url}avatar?username=${username}`,
      "/images/default_avatar.png",
    );
    banner = await fetchURL(
      `${url}banner?username=${username}`,
      "/images/default_banner.png",
    );
    publicationElements = updatePublicationElements(publications);
    updateSelectedPublication(publications[0]);
    console.log(avatar, banner);

    bio = await fetchInfo(`${url}description?username=${username}`).then(
      (response) => response.desc,
    );
  });
</script>

<section class="container">
  <div class="row mt-4 h-100 pb-3">
    <div class="col-sm-1 side-menu main-side-menu">
      <Sidemenu elements={sections} on:menuClick={handleMainMenuClick} />
    </div>
    <div class="col modal-content h-100 new-pub-form-wrap">
      {#if selectedSection === "new"}
        <div class="new-pub-form h-100">
          <NewPubForm on:componentUpdate={sendComponentUpdate} />
        </div>
      {:else if selectedPublication && selectedSection === "edit"}
        <div class="row h-100">
          {#if publications.length > 0}
            <div class="col-sm-3 h-100 side-menu edit-side-menu">
              <nav id="sidebarMenu" class="d-lg-block sidebar h-100">
                <div class="position-sticky h-100">
                  <div class="list-group list-group-flush mr-3 h-100">
                    {#if publications}
                      <Sidemenu
                        searchMenu={true}
                        bind:updateElements={updateEditMenu}
                        elements={publicationElements}
                        on:menuClick={handleEditMenuClick}
                      />
                    {/if}
                  </div>
                </div>
              </nav>
            </div>
          {/if}
          <div
            class="col modal-content h-100 edit-content-wrap d-flex flex-column"
          >
            <div class="edit-content h-100 px-3">
              {#if publications.length > 0}
                <EditPubForm
                  on:componentUpdate={sendComponentUpdate}
                  publication={selectedPublication}
                />
              {/if}
            </div>
          </div>
        </div>
      {:else if selectedSection === "edit"}
        <div class="edit-content h-100 px-3">
          <h2 class="mt-3 text coolvetica">No publications</h2>
        </div>
      {:else if selectedSection === "bio"}
        <div
          class="col modal-content h-100 edit-content-wrap d-flex flex-column"
        >
          <UserBioForm
            on:componentUpdate={sendComponentUpdate}
            {username}
            {bio}
          />
        </div>
      {:else if selectedSection === "avatar"}
        <div
          class="col modal-content h-100 edit-content-wrap d-flex flex-column"
        >
          <UpdateImageForm
            on:componentUpdate={sendComponentUpdate}
            {username}
            contentType="avatar"
            content={avatar}
          />
        </div>
      {:else if selectedSection === "banner"}
        <div
          class="col modal-content h-100 edit-content-wrap d-flex flex-column"
        >
          <UpdateImageForm
            on:componentUpdate={sendComponentUpdate}
            {username}
            contentType="banner"
            content={banner}
          />
        </div>
      {:else if selectedSection === "sign out"}
        <UserLogout />
      {/if}
    </div>
  </div>
</section>

<style lang="scss">
  section {
    height: 75vh;
  }
  .main-side-menu {
    width: 9%;
  }

  .side-menu {
    padding-left: 0;
    padding-right: 0;
  }

  .edit-content,
  .edit-side-menu {
    padding-left: 0.75em;
  }

  .edit-content,
  .new-pub-form {
    border-radius: 20px;
    background-color: var(--surface);
  }

  .edit-content-wrap {
    background-color: var(--surface);
    border-radius: 20px;
  }
</style>
