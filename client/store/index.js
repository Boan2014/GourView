import { type } from "os";

export const strict = false;

const　initialState = {
  name: '',
  predictLabel: [],
  posPercent : "",
  negPercent : "", 
  posRev : "",
  negRev : "",
};

export const state = () => Object.assign({}, initialState);

export const mutations ={
    setPredictLabel (state, predictLabel) {
      state.predictLabel = predictLabel[0]
      state.posPercent = predictLabel[1][0]
      state.negPercent = predictLabel[1][1]
      state.posRev = predictLabel[1][2]
      state.negRev = predictLabel[1][3]
    },
    clear(state) {
      for (let key in state) {
        if (initialState.hasOwnProperty(key)) {
          state[key] = initialState[key];
        }
      }
    }
  };