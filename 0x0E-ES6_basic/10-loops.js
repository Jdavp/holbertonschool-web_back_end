export default function appendToEachArrayValue(array, appendString) {
  let tempArray = array;
  for (let element of array) {
    let idx = array.indexOf(element);
    tempArray[idx] = `${appendString}${element}`;
  }

  return tempArray;
}
