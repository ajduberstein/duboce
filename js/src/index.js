import * as Plot from "@observablehq/plot";
import { JSONConverter } from "@deck.gl/json";

function namedDataShim(cls) {
  // @deck.gl/json only works with named arguments
  class WrappedPlot {
    constructor({ data, options }, ...args) {
      return new cls(data, options, ...args);
    }
  }
  return WrappedPlot;
}

// Grafted https://github.com/visgl/deck.gl/blob/master/modules/jupyter-widget/src/playground/create-deck.js
function extractClasses(library = {}) {
  // Extracts exported class constructors as a dictionary from a library
  const classesDict = {};
  const classes = Object.keys(library).filter(
    (x) => x.charAt(0) === x.charAt(0).toUpperCase()
  );
  for (const cls of classes) {
    const unwrapped = library[cls];
    classesDict[cls] = namedDataShim(unwrapped);
  }
  return classesDict;
}

// Handle JSONConverter and loaders configuration
const jsonConverterConfiguration = {
  classes: extractClasses(Plot),
};

const jsonConverter = new JSONConverter({
  configuration: jsonConverterConfiguration,
});

export { jsonConverter };
