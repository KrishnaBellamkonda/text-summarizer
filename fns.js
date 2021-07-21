/* This is to save all the functions related to the web application */

// const sendPostRequest = async (preprocessed_inputs) => {

//     try {
//         const resp = await axios.post(SERVER_URL, preprocessed_inputs);
//         console.log(resp.data);
//         outputs = resp.data;
//     } catch (e) {
//         console.error(e);
//     }


// axios.post(SERVER_URL, preprocessed_inputs)
// .then((res) => {
//     console.log("THE POST REQUEST SUCCEEDED!");
//     //console.log(res.data);
//     outputs = res.data["outputs"];
//     console.log(outputs);
// }, (error) => {
//     console.log("THE POST REQUEST FAILED:<!");
//     console.log(error);
// });