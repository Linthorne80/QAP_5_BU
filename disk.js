fetch('./people.js')
  .then(response => response.json())
  .then(people => {
    // Loop through an array in the JSON data
    people.forEach(person => {
       changeRoom(person);
    });
  })
  .catch(error => {
    // Handle any errors that occur while fetching the file
    console.error(error);
  });


  function changeRoom(person) {
    switch(person.gender){
      case "female": 
        console.log(`${person.fname} should use the female change room.`);
        break;
      case "non-binary": 
        console.log(`${person.fname} should use the inclusive change room.`);
        break;
      case "male":
        console.log(`${person.fname} should use the male change room.`);
        break;
      default:
        console.log(`${person.fname} should be mindful in choosing a change room.`);
    }
  };