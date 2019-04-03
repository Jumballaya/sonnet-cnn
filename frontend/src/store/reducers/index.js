import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
import { reducer as sonnet } from './sonnet';
import { reducer as imagenet } from './imagenet';

export default history =>
  combineReducers({
    router: connectRouter(history),
    sonnet,
    imagenet,
  });
