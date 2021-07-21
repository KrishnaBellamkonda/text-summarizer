/*
This web application takes in a paragraph and the outputs a
extractive summary produced by a neural network
*/

var fs = require("fs");
var axios = require("axios").default;
const util = require("util");
const exec = util.promisify(require("child_process").exec);
const SERVER_URL = 'http://localhost:8501/v1/models/text_summarizer:predict';
// Utility Functions

async function executePreprocessing(){
    try {
        const {stdout, stderr} = await exec("python preprocessing/preprocessing_main.py");
        console.log(stdout);
        console.log(stderr);
    } catch (e) {
        console.log(e);
}
};

function readJSON(path){
    var data_string = fs.readFileSync(path);
    var data = JSON.parse(data_string);
    return data
};

async function writeJSONString(object, path="./input_data/string.json"){
    fs.writeFile(path, JSON.stringify(object), (err) => {
        if (err) console.log(err);
        else {
            console.log("String JSON File written successfully!")
        }
    });
}

// async function executePreprocessing(){
//     exec("python preprocessing/preprocessing_main.py");
// };

function argsort(arrayObj){
    const arrayObject = arrayObj.map((value, idx) => {
        return {value, idx};
    });

    arrayObject.sort((a, b) => {
        if (a.value < b.value){
            return -1
        }

        if (a.value > b.value) {
            return 1;
        }

        return 0;
    });

    const argIndices = arrayObject.map(data => data.idx);
    return argIndices;
}

function makePostRequest(inputs){
    return new Promise(function(resolve, reject) {
        axios.post(SERVER_URL, inputs).then(
            (response) => {
                var result = response.data;
                console.log('Processing Request');
                resolve(result);
            }, (error) => {
                reject(error);
            }
        );
    }
    );
}



async function receivePredictions(inputs){
var outputs = await makePostRequest(inputs);
return outputs
}


// Loading the preprocessed inputs
var preprocessed_inputs = readJSON('input_data/preprocessed_string.json');
// Sending a POST request
    // Converting this into an asynchronous function 



// }


async function main(){
    var express = require('express');
    var app = express();
    app.set('view engine', "ejs");
    const path = require('path');
    const port = 5000;

    app.use(express.static('public'));

    app.use("/loading", async (req, res)=>{
        body = req.query.data;
        console.log(body);
        string_object = {string:body};
        await writeJSONString(string_object);
        await executePreprocessing();
        //console.log(body);
        var preprocessed_inputs = await readJSON('input_data/preprocessed_string.json');
        outputs = await receivePredictions(preprocessed_inputs);
        console.log(outputs);
        if (outputs != null) res.redirect("/summary");
    })

    app.use("/summary", async (req, res) => {
        data_string_obj = await readJSON('input_data/sentences_list.json');
        data_string_list = data_string_obj["sentences"];
        //console.log(data_string_list);
        var indices = argsort(outputs["outputs"]);
        res.render('summary', {body:body, indices:indices, data_string_list:data_string_list});
    });

    app.get('*',function (req, res) {
        res.redirect('/home.html');
        
    });

    app.listen(5000, (req, res) => {
        console.log("Listening on port 5000");
    });
}
main();