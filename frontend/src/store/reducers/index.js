import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
import { reducer as sonnet } from './sonnet';

export default history =>
  combineReducers({
    router: connectRouter(history),
    sonnet,
  });
