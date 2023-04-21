import axios from "axios";
import React from "react";

class NeuralSearch extends React.Component {
  state = {
    inputString: "",
    prediction: "",
  };

  handleChange = (event) => {
    this.setState({ inputString: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();

    axios
      .post("/api/predict", {
        inputString: this.state.inputString,
      })
      .then((response) => {
        this.setState({ prediction: response.data.prediction });
      })
      .catch((error) => {
        console.error(error);
      });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Input String:
          <input
            type="text"
            value={this.state.inputString}
            onChange={this.handleChange}
          />
        </label>
        <button type="submit">Predict</button>
        <p>Prediction: {this.state.prediction}</p>
      </form>
    );
  }
}
