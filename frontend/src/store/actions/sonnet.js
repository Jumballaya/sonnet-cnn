import API from '../../api/sonnet';

export const FETCH_SONNET = 'FETCH_SONNET';
export const FETCH_SONNET_SUCCESS = 'FETCH_SONNET_SUCCESS';
export const FETCH_SONNET_FAILURE = 'FETCH_SONNET_FAILURE';

const fetchSonnetStart = () => ({
  type: FETCH_SONNET,
});

const fetchSonnetSuccess = movies => ({
  type: FETCH_SONNET_SUCCESS,
  payload: movies,
});

const fetchSonnetFailure = error => ({
  type: FETCH_SONNET_FAILURE,
  payload: error,
});

export const fetchSonnet = () => dispatch => {
  dispatch(fetchSonnetStart());
  API.generate().then(
    res => dispatch(fetchSonnetSuccess(res)),
    err => dispatch(fetchSonnetFailure(err))
  );
};
