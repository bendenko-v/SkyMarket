import React, { useState, useContext } from "react";
import AuthContext from "../../context/AuthContext";
import Form from "../form/Form";
import useFormValidation from "../../utils/hooks/useFormValidation";

function Login(props) {
  const [input, setInput] = useState("");
  const { values, handleChange, errors, isValid } = useFormValidation();
  let { loginUser } = useContext(AuthContext);

  function handleChangeInput(e) {
    handleChange(e);
    if (input.length > 0) {
      setInput("");
    }
  }

  return (
    <Form
      header="Glad to see you!"
      onSubmit={loginUser}
      path="/profile"
      btn="Sign in"
      link="/sign-up"
      linkTitle="Sign up"
      newPassword="Restore password"
      errors={!isValid}
    >
      <>
        <label className="form__label">
          <h2 className="form__description">E-mail</h2>
          <input
            required
            name="email"
            type="email"
            value={values.email || ""}
            pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
            autoComplete="on"
            className="form__email form__input"
            onChange={handleChangeInput}
          />
          <div
            className={`input-hidden ${
              errors.email ? "input-error" : ""
            }`}
          >
            {errors.email}
          </div>
        </label>
        <label className="form__label">
          <h2 className="form__description">Password</h2>
          <input
            required
            value={values.password || ""}
            name="password"
            type="password"
            minLength="1"
            autoComplete="on"
            className="form__password form__input"
            onChange={handleChangeInput}
          />
          <div
            className={`input-hidden ${
              errors.password ? "input-error" : ""
            }`}
          >
            {errors.password}
          </div>
        </label>
      </>
    </Form>
  );
}

export default Login;
