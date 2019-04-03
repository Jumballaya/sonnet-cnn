import API from '../../api/imagenet';

export const FETCH_IMAGENET = 'FETCH_IMAGENET';
export const FETCH_IMAGENET_SUCCESS = 'FETCH_IMAGENET_SUCCESS';
export const FETCH_IMAGENET_FAILURE = 'FETCH_IMAGENET_FAILURE';

const fetchImagenetStart = () => ({
  type: FETCH_IMAGENET,
});

const fetchImagenetSuccess = movies => ({
  type: FETCH_IMAGENET_SUCCESS,
  payload: movies,
});

const fetchImagenetFailure = error => ({
  type: FETCH_IMAGENET_FAILURE,
  payload: error,
});

export const fetchImagenet = img => dispatch => {
  dispatch(fetchImagenetStart());
  API.predict(img).then(
    res => dispatch(fetchImagenetSuccess(res)),
    err => dispatch(fetchImagenetFailure(err))
  );
};
