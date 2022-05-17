import { Container, Navbar } from "react-bootstrap";
import { NavigationBar } from "./NavigationBar";

export const Header = () => {
  return (
    <Navbar role="navigation" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/">
        </Navbar.Brand>
        <Navbar.Collapse className="navbar-right">
          <NavigationBar />
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
