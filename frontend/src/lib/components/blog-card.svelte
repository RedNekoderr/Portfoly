<script lang="ts">
  import {
    Brush,
    PcDisplayHorizontal,
    Calendar2Event,
    TextParagraph,
  } from "svelte-bootstrap-icons";
  import { Modal } from "svelte-simple-modal";
  import ContentReadMore from "./modal/contentReadMore.svelte";
  import CustomCloseButton from "./modal/customCloseButton.svelte";
  import type { Publication } from "./types/publication.svelte";

  export let publication: Publication;

  let cardHeader: HTMLDivElement;
</script>

<div class="col-lg-5 d-flex justify-content-center mb-5">
  <div class="card neo-ov p-3 w-100">
    <div bind:this={cardHeader} class="card-header mx-3 my-2 p-0">
      <div
        class="image-container w-100 h-100 d-flex align-items-center m-0 p-0"
        style="background-image: url({publication.blob});"
      >
        <img
          class="card-img-top m-0 p-0"
          src={publication.blob}
          alt="Card header"
        />
      </div>
    </div>
    <div class="card-body pt-2">
      <div class="media d-flex align-items-center justify-content-between">
        <div class="post-group">
          <span
            data-toggle="tooltip"
            data-placement="top"
            title=""
            data-original-title="test"
            class="text"
          >
            <img src="" alt="" />
            {#if publication.pubType === "it"}
              <PcDisplayHorizontal width="18" height="18" />
            {:else if publication.pubType === "art"}
              <Brush width="18" height="18" />
            {:else}
              <TextParagraph width="18" height="18" />
            {/if}
          </span>
        </div>
        <div class="d-flex align-items-center">
          <div style="position: relative; top: -2px; left: -4px">
            <Calendar2Event width="18" height="18" />
          </div>
          <span>
            {publication.date}
          </span>
        </div>
      </div>
      <div class="d-flex flex-column align-items-start">
        <h3 class="text h5 card-title mt-4">{publication.title}</h3>
        <p class="text subtle card-text text-start">
          {publication.shortDesc}
        </p>
        <Modal
          closeButton={CustomCloseButton}
          classWindow="relative w-75 max-w-full h-100 my-2 mx-auto rounded shadow-md base-forced"
          ><ContentReadMore {publication} /></Modal
        >
      </div>
    </div>
  </div>
</div>

<style>
  .card {
    outline: none;
    border: none;
  }

  .card-header {
    height: 250px;
  }
  .image-container {
    position: relative;
    overflow: hidden;
    border-radius: 1em;
  }

  .image-container::before {
    content: "";
    position: absolute;
    background-size: cover;
    background-repeat: no-repeat;
    background-image: inherit;
    filter: brightness(0.7) blur(5px);
    height: 100%;
    width: 100%;
  }

  .image-container img {
    position: relative;
    border-radius: 1em;
  }

  .card-header {
    background: transparent;
    border: none;
  }
  .post-group span {
    font-size: 1em;
    text-decoration: none;
  }
</style>
