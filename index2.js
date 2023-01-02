function getRandomInt(min, max, numbersToExclude) {
    min = Math.ceil(min)
    max = Math.floor(max)
}
    const random = Math.floor(Math.random() * (max - min) + min)
    return numbersToExclude.has(random) ?
      getRandomInt(min, max, numbersToExclude)  
