import { applyMiddleware, compose, createStore } from 'redux';
import thunk from 'redux-thunk';
import { connectedRouter, routerMiddleware } from 'connected-react-router';
import rootReducer from './reducers';

export default function configureStore(history, initialState) {
  // In development, use the browser's Redux dev tools extension if installed
  const enhancers = [];
  const isDevelopment = process.env.NODE_ENV === 'development';
  const hasWindow = typeof window !== 'undefined';
  const hasTools = window.devToolsExtension;
  const useDevTools = isDevelopment && hasWindow && hasTools;
  if (useDevTools) enhancers.push(window.devToolsExtension());

  // Middleware
  const middleware = [thunk, routerMiddleware(history)];

  // Create the store and return it
  return createStore(
    rootReducer(history),
    initialState,
    compose(
      applyMiddleware(...middleware),
      ...enhancers
    )
  );
}
