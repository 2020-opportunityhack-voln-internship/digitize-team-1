import React, { Component } from "react";
import axios from 'axios'
import {
  Row,
  Col
} from "reactstrap";

class UploadForm extends Component {
    /*  Component renders form that npo accounts can user to upload images of paper forms and then sends the form to the api where it gets stored */

    state = {
      paper_form: null,
      title: ''
  };

  handleImageChange = (event) => {
    /*updates state to contain selected file and its name */
    this.setState({
      paper_form: event.target.files[0],
      title: event.target.files[0].name
    })
  };

  handleSubmit = (event) => {
    /* Sends file to api using axios */

    event.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('paper_form', this.state.paper_form);
    form_data.append('title', this.state.title);
    let url = 'http://127.0.0.1:8000/api/upload/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };

  render() {
    /* Front end rendering */
    return (
      <div>
        <h1>Upload</h1>
        <form onSubmit={this.handleSubmit} /*action="/upload" method="POST"*/ >
          <label>
            Upload File:
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
            <br/>
            <input type="submit" value="Submit"/>
          </label>
        </form>
      </div>
    );
  }
}

export default UploadForm;
