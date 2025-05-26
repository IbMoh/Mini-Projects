import fs from 'fs'

const lis = []

try{

    fs.readFile('dictionary.txt', (err, data) => {
        if (err) throw err

        for(x in data){
            lis.push(x)
        }

    })
}catch(error){
    console.error(error)
}

console.log(dict)