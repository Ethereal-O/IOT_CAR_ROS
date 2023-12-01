import React from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom';
import { history } from "./utils/history";
import Sender from "./views/sender";

class BasicRoute extends React.Component {

    constructor(props) {
        super(props);

        history.listen((location, action) => {
            // clear alert on location change
            console.log(location, action);
        });
    }

    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route exact path="/" component={Sender} />
                    <Redirect from="/*" to="/" />
                </Switch>
            </Router>
        )
    }


}

export default BasicRoute;