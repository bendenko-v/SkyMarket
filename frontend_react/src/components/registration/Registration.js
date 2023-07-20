import React, { useState, useContext } from "react";
import Form from "../form/Form";
import AuthContext from "../../context/AuthContext";
import useFormValidation from "../../utils/hooks/useFormValidation";

function Registration() {
  const [input, setInput] = useState("");
  const { values, handleChange, errors, isValid } = useFormValidation();
  let { register } = useContext(AuthContext);

  function handleChangeInput(e) {
    handleChange(e);
    if (input.length > 0) {
      setInput("");
    }
  }

  return (
    <Form
      header="Welcome!"
      onSubmit={register}
      path="/sign-in"
      btn="Sign up"
      text="Already registered?&nbsp;"
      link="/sign-in"
      linkTitle="Sign in"
      errors={!isValid}
    >
      <>
        <label className="form__label">
          <h2 className="form__description">First name</h2>
          <input
            required
            value={values.first_name || ""}
            title="First name"
            name="first_name"
            type="text"
            minLength="3"
            className="form__input"
            maxLength="30"
            onChange={handleChangeInput}
          />
          <div
            className={`input-hidden ${
              errors.first_name ? "input-error" : ""
            }`}
          >
            {errors.first_name}
          </div>
        </label>
        <label className="form__label">
          <h2 className="form__description">Surname</h2>
          <input
            required
            value={values.last_name || ""}
            title="Surname"
            name="last_name"
            type="text"
            minLength="3"
            className="form__input"
            maxLength="30"
            onChange={handleChangeInput}
          />
          <div
            className={`input-hidden ${
              errors.last_name ? "input-error" : ""
            }`}
          >
            {errors.last_name}
          </div>
        </label>
        <label className="form__label">
          <h2 className="form__description">E-mail</h2>
          <input
            required
            value={values.email || ""}
            name="email"
            type="email"
            pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
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
            minLength="8"
            placeholder="the password must consist of letters and numbers"
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
        <label className="form__label">
          <h2 className="form__description">Phone</h2>
          <input
            required
            value={values.phone || ""}
            title="Phone"
            type="tel"
            name="phone"
            pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"
            placeholder="+7(___)___-__-__"
            className="form__input"
            onChange={handleChangeInput}
          />
          <div
            className={`input-hidden ${
              errors.phone ? "input-error" : ""
            }`}
          >
            {errors.phone}
          </div>
        </label>
      </>
    </Form>
  );
}

export default Registration;
