import figlet from "figlet";

async function doStuff() {
  const text = await figlet.text("EVOLVE AI");
  console.log(text);
}

doStuff();