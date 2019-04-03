import {
  FETCH_IMAGENET,
  FETCH_IMAGENET_SUCCESS,
  FETCH_IMAGENET_FAILURE,
} from '../actions/imagenet';

const initialState = {
  images: [],
  errors: [],
  loading: false,
};

export const reducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_IMAGENET:
      return {
        ...state,
        loading: true,
        errors: [],
      };

    case FETCH_IMAGENET_SUCCESS:
      return {
        ...state,
        loading: false,
        images: [...state.images, action.payload],
        errors: [],
      };

    case FETCH_IMAGENET_FAILURE:
      return {
        ...state,
        loading: false,
        errors: action.payload,
      };

    default:
      return state;
  }
};
