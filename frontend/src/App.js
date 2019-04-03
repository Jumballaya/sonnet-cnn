import React from 'react';
import { Route, Switch } from 'react-router';
import Layout from './views/Layout';
import Home from './views/Home';
import Sonnet from './views/Sonnet';

export default () => (
  <Layout>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/sonnet" component={Sonnet} />
    </Switch>
  </Layout>
);
