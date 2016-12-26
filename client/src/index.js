/**
 * PriceHike client main entry point
 *
 * @flow
 */

import HotReloader from 'systemjs-hot-reloader/hot-reloader';
new HotReloader('https://localhost:3000');

import React from 'react';
import ReactDOM from 'react-dom';

export function __reload(m) {
  if (m.component.state)
    component.setState(m.component.state);
}

export let component = ReactDOM.render(<div>{'Hello world 21az'}</div>, document.getElementById('root'));
