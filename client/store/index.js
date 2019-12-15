import { type } from "os";

export const strict = false;

const　initialState = {
  name: '',
  predictLabel: [],
  posPercent : "",
  negPercent : "", 
  shopName : "",
};

export const state = () => Object.assign({}, initialState);

export const mutations ={
    setPredictLabel (state, predictLabel) {
      state.predictLabel = predictLabel[0]
      state.posPercent = predictLabel[1][0]
      state.negPercent = predictLabel[1][1]
      state.shopName = predictLabel[2]
    },
    clear(state) {
      for (let key in state) {
        if (initialState.hasOwnProperty(key)) {
          state[key] = initialState[key];
        }
      }
    }
  };