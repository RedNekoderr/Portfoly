<script lang="ts">
  import { createEventDispatcher, onMount } from "svelte";
  import { getAllProps } from "./types/elementInfo.svelte";
  import type { Element } from "./types/elementInfo.svelte";

  const dispatch = createEventDispatcher();

  export let searchMenu: boolean = false;
  export let elements: Array<Element> = [];
  export let selectedSection: string = elements[0].name;
  let selectedIndex: number = 0;

  let selectedElements: Array<Element> = elements;
  let filterType: string = "all";
  let filterName: string = "";

  function handleMenuClick(event: Event) {
    const button = event.target as HTMLButtonElement;
    const buttons = button.closest("nav")?.querySelectorAll("button");

    if (buttons) {
      buttons.forEach((btn) => {
        if (btn !== button) {
          btn.classList.remove("selected");
        }
      });
      button.classList.add("selected");
      selectedSection = button.id;
      selectedIndex = elements.findIndex(
        (element) =>
          element.name.toLowerCase() === selectedSection.toLowerCase(),
      );
      dispatch("menuClick", selectedSection);
    }
  }

  function unselectElements() {
    for (let element of selectedElements) {
      document
        .getElementById(element.name.toLowerCase())
        ?.classList.remove("selected");
    }
  }

  export let updateElements = (
    newElements: Array<Element>,
    detail: string = "",
  ) => {
    if (detail === "removePublication") {
      if (selectedIndex) {
        selectedIndex--;
        selectNthElement(selectedIndex);
      } else if (elements.length > 1) {
        selectNthElement(selectedIndex);
        selectedIndex++;
      }
    }
    selectedSection = elements[selectedIndex].name;
    elements = newElements;
    selectedElements = elements;
    filterElements();
    dispatch("menuClick", selectedSection);
  };

  export let selectNthElement = (n: number) => {
    unselectElements();
    if (0 <= n && n <= selectedElements.length && elements.length > 0) {
      const button = document.getElementById(elements[n].name.toLowerCase());
      button?.classList.add("selected");
    }
  };

  function filterElements() {
    selectedElements = elements.filter((element) => {
      if (filterType === "all" || element.info.includes(filterType)) {
        return element.name.toLowerCase().includes(filterName.toLowerCase());
      }
      return false;
    });
  }

  onMount(() => {
    if (elements.length > 0) {
      selectNthElement(0);
    }
  });

  $: {
    filterElements();
    filterName, filterType, elements, selectedElements, updateElements;
  }
</script>

<nav id="sideBar" class="collapse d-lg-block sidebar collapse h-100 py-3">
  <div class="position-sticky">
    <div class="list-group list-group-flush mx-3">
      {#if searchMenu}
        <div class="row mb-2 p-2 mx-1 search-menu">
          <div class="col">
            <select
              bind:value={filterType}
              class="form-select"
              name="type"
              id="type"
            >
              <option value="all">All</option>
              {#each getAllProps(elements) as prop}
                <option value={prop}
                  >{prop.charAt(0).toUpperCase() + prop.slice(1)}</option
                >
              {/each}
            </select>
          </div>
          <div class="col">
            <input
              bind:value={filterName}
              type="text"
              class="form-control"
              placeholder="Search"
            />
          </div>
        </div>
      {/if}
      <div class="row">
        <div class="col d-flex flex-column">
          {#each selectedElements as element}
            <button
              on:click={handleMenuClick}
              id={element.name.toLowerCase()}
              class="text button my-1"
            >
              {element.name}</button
            >
          {/each}
        </div>
      </div>
    </div>
  </div>
</nav>

<style>
  .sidebar {
    background-color: var(--panel);
    border-radius: 20px;
  }

  .button {
    font-size: 1em;
  }

  .button {
    background-color: var(--base);
  }

  .button:hover {
    background-color: var(--highlight-mid);
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

  .search-menu {
    background-color: var(--highlight-low);
    border-radius: 10px;
  }
</style>
