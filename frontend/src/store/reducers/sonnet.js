import {
  FETCH_SONNET,
  FETCH_SONNET_SUCCESS,
  FETCH_SONNET_FAILURE,
} from '../actions/sonnet';

const initialState = {
  sonnet: '',
  errors: [],
  loading: false,
};

export const reducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_SONNET:
      return {
        ...state,
        loading: true,
        errors: [],
      };

    case FETCH_SONNET_SUCCESS:
      return {
        ...state,
        loading: false,
        sonnet: action.payload,
        errors: [],
      };

    case FETCH_SONNET_FAILURE:
      return {
        ...state,
        loading: false,
        sonnet: '',
        errors: action.payload,
      };

    default:
      return state;
  }
};
