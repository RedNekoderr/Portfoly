<script context="module" lang="ts">
  export interface Element {
    name: string;
    info: Array<string>;
  }

  export function createElement(name: string, info: Array<string>): Element {
    let element: Element = { name, info };
    return element;
  }

  export function getAllProps(elements: Array<Element>) {
    let props = new Array();
    for (let element of elements) {
      for (let prop of element.info) {
        if (!props.includes(prop)) {
          props.push(prop);
        }
      }
    }
    return props;
  }
</script>
