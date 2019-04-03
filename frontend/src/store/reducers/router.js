import { connectedRouter } from 'connected-react-router';

export default function configureStore(history, initialState) {
  const middleware = [thunk];

  // In development, use the browser's Redux dev tools extension if installed
  const enhancers = [];
  const isDevelopment = process.env.NODE_ENV === 'development';

  // Create browser history
  const baseUrl = document.getElementsByTagName('base')[0].getAttribute('href');
  const history = createBrowserHistory({ basename: baseUrl });

  if (
    isDevelopment &&
    typeof window !== 'undefined' &&
    window.devToolsExtension
  ) {
    enhancers.push(window.devToolsExtension());
  }

  const rootReducer = combineReducers({
    router: connectRouter(history),
    ...reducers,
  });

  return createStore(
    rootReducer,
    initialState,
    compose(
      applyMiddleware(...middleware),
      ...enhancers
    )
  );
}
