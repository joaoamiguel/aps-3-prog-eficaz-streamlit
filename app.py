import streamlit as st
import requests
from bson import ObjectId

# URL da API Flask (substitua pela URL do seu backend)
API_URL = "https://aps-3-flask-rest-mongo.onrender.com"

st.set_page_config(page_title="Aluguel de Bicicletas Compartilhadas", layout="wide")

st.title("Sistema de Aluguel de Bicicletas Compartilhadas")

menu = ["Usuários", "Bicicletas", "Empréstimos"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------- USUÁRIOS --------------------
if choice == "Usuários":
    st.header("Gerenciar Usuários")

    # Sub-seção: Adicionar Novo Usuário
    st.subheader("Adicionar Novo Usuário")
    with st.form(key='add_user_form'):
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        data_nascimento = st.text_input("Data de Nascimento (YYYY-MM-DD)")
        submit_add_user = st.form_submit_button("Adicionar Usuário")

    if submit_add_user:
        if not nome or not cpf or not data_nascimento:
            st.error("Todos os campos são obrigatórios.")
        else:
            payload = {
                "nome_usuario": nome,
                "cpf": cpf,
                "data_nascimento": data_nascimento
            }
            response = requests.post(f"{API_URL}/usuarios", json=payload)
            if response.status_code == 201:
                st.success("Usuário adicionado com sucesso!")
            else:
                st.error(response.json().get("erro", "Erro ao adicionar usuário."))

    st.markdown("---")

    # Sub-seção: Lista de Usuários
    st.subheader("Lista de Usuários")
    response = requests.get(f"{API_URL}/usuarios")
    if response.status_code == 200:
        usuarios = response.json().get("usuarios", [])
        if usuarios:
            for user in usuarios:
                st.write(f"**ID:** {user.get('_id')}")
                st.write(f"**Nome:** {user.get('nome_usuario')}")
                st.write(f"**CPF:** {user.get('cpf')}")
                st.write(f"**Data de Nascimento:** {user.get('data_nascimento')}")
                st.write("---")
        else:
            st.info("Nenhum usuário encontrado.")
    else:
        st.error(response.json().get("error", "Erro ao buscar usuários."))

    st.markdown("---")

    # Sub-seção: Atualizar Usuário
    st.subheader("Atualizar Usuário")
    with st.form(key='update_user_form'):
        user_id = st.text_input("ID do Usuário")
        novo_nome = st.text_input("Novo Nome")
        novo_cpf = st.text_input("Novo CPF")
        nova_data_nascimento = st.text_input("Nova Data de Nascimento (YYYY-MM-DD)")
        submit_update_user = st.form_submit_button("Atualizar Usuário")

    if submit_update_user:
        if not user_id or not novo_nome or not novo_cpf or not nova_data_nascimento:
            st.error("Todos os campos são obrigatórios.")
        else:
            payload = {
                "nome_usuario": novo_nome,
                "cpf": novo_cpf,
                "data_nascimento": nova_data_nascimento
            }
            response = requests.put(f"{API_URL}/usuarios/{user_id}", json=payload)
            if response.status_code == 200:
                st.success("Usuário atualizado com sucesso!")
            else:
                st.error(response.json().get("error", "Erro ao atualizar usuário."))

    st.markdown("---")

    # Sub-seção: Deletar Usuário
    st.subheader("Deletar Usuário")
    with st.form(key='delete_user_form'):
        delete_user_id = st.text_input("ID do Usuário a Deletar")
        submit_delete_user = st.form_submit_button("Deletar Usuário")

    if submit_delete_user:
        if not delete_user_id:
            st.error("O ID do usuário é obrigatório.")
        else:
            response = requests.delete(f"{API_URL}/usuarios/{delete_user_id}")
            if response.status_code == 200:
                st.success("Usuário deletado com sucesso!")
            else:
                st.error(response.json().get("error", "Erro ao deletar usuário."))

# -------------------- BICICLETAS --------------------
elif choice == "Bicicletas":
    st.header("Gerenciar Bicicletas")

    # Sub-seção: Adicionar Nova Bicicleta
    st.subheader("Adicionar Nova Bicicleta")
    with st.form(key='add_bike_form'):
        marca = st.text_input("Marca")
        modelo = st.text_input("Modelo")
        cidade = st.text_input("Cidade")
        status = st.selectbox("Status", ["disponivel", "em uso"])
        submit_add_bike = st.form_submit_button("Adicionar Bicicleta")

    if submit_add_bike:
        if not marca or not modelo or not cidade or not status:
            st.error("Todos os campos são obrigatórios.")
        else:
            payload = {
                "marca": marca,
                "modelo": modelo,
                "cidade": cidade,
                "status": status
            }
            response = requests.post(f"{API_URL}/bikes", json=payload)
            if response.status_code == 201:
                st.success("Bicicleta adicionada com sucesso!")
            else:
                st.error(response.json().get("erro", "Erro ao adicionar bicicleta."))

    st.markdown("---")

    # Sub-seção: Lista de Bicicletas
    st.subheader("Lista de Bicicletas")
    response = requests.get(f"{API_URL}/bikes")
    if response.status_code == 200:
        bikes = response.json().get("bikes", [])
        if bikes:
            for bike in bikes:
                st.write(f"**ID:** {bike.get('_id')}")
                st.write(f"**Marca:** {bike.get('marca')}")
                st.write(f"**Modelo:** {bike.get('modelo')}")
                st.write(f"**Cidade:** {bike.get('cidade')}")
                st.write(f"**Status:** {bike.get('status')}")
                st.write("---")
        else:
            st.info("Nenhuma bicicleta encontrada.")
    else:
        st.error(response.json().get("error", "Erro ao buscar bicicletas."))

    st.markdown("---")

    # Sub-seção: Atualizar Bicicleta
    st.subheader("Atualizar Bicicleta")
    with st.form(key='update_bike_form'):
        bike_id = st.text_input("ID da Bicicleta")
        nova_marca = st.text_input("Nova Marca")
        novo_modelo = st.text_input("Novo Modelo")
        nova_cidade = st.text_input("Nova Cidade")
        novo_status = st.selectbox("Novo Status", ["disponivel", "em uso"])
        submit_update_bike = st.form_submit_button("Atualizar Bicicleta")

    if submit_update_bike:
        if not bike_id or not nova_marca or not novo_modelo or not nova_cidade or not novo_status:
            st.error("Todos os campos são obrigatórios.")
        else:
            payload = {
                "marca": nova_marca,
                "modelo": novo_modelo,
                "cidade": nova_cidade,
                "status": novo_status
            }
            response = requests.put(f"{API_URL}/bikes/{bike_id}", json=payload)
            if response.status_code == 200:
                st.success("Bicicleta atualizada com sucesso!")
            else:
                st.error(response.json().get("error", "Erro ao atualizar bicicleta."))

    st.markdown("---")

    # Sub-seção: Deletar Bicicleta
    st.subheader("Deletar Bicicleta")
    with st.form(key='delete_bike_form'):
        delete_bike_id = st.text_input("ID da Bicicleta a Deletar")
        submit_delete_bike = st.form_submit_button("Deletar Bicicleta")

    if submit_delete_bike:
        if not delete_bike_id:
            st.error("O ID da bicicleta é obrigatório.")
        else:
            response = requests.delete(f"{API_URL}/bikes/{delete_bike_id}")
            if response.status_code == 200:
                st.success("Bicicleta deletada com sucesso!")
            else:
                st.error(response.json().get("error", "Erro ao deletar bicicleta."))

# -------------------- EMPRÉSTIMOS --------------------
elif choice == "Empréstimos":
    st.header("Gerenciar Empréstimos")

    # Sub-seção: Registrar Novo Empréstimo
    st.subheader("Registrar Novo Empréstimo")
    with st.form(key='add_loan_form'):
        # Buscar usuários disponíveis
        users_response = requests.get(f"{API_URL}/usuarios")
        users = users_response.json().get("usuarios", []) if users_response.status_code == 200 else []

        # Buscar bicicletas disponíveis
        bikes_response = requests.get(f"{API_URL}/bikes")
        available_bikes = [bike for bike in bikes_response.json().get("bikes", []) if bike.get("status") == "disponivel"] if bikes_response.status_code == 200 else []

        if not users:
            st.warning("Nenhum usuário disponível para empréstimo.")
        if not available_bikes:
            st.warning("Nenhuma bicicleta disponível para empréstimo.")

        if users and available_bikes:
            user_options = {f"{user['nome_usuario']} (CPF: {user['cpf']})": user['_id'] for user in users}
            bike_options = {f"{bike['marca']} {bike['modelo']} (ID: {bike['_id']})": bike['_id'] for bike in available_bikes}

            selected_user = st.selectbox("Selecionar Usuário", list(user_options.keys()))
            selected_bike = st.selectbox("Selecionar Bicicleta", list(bike_options.keys()))
            data_aluguel = st.date_input("Data de Aluguel").strftime("%Y-%m-%d")
            submit_add_loan = st.form_submit_button("Registrar Empréstimo")

            if submit_add_loan:
                user_id = user_options[selected_user]
                bike_id = bike_options[selected_bike]
                payload = {
                    "data_aluguel": data_aluguel
                }
                response = requests.post(f"{API_URL}/emprestimos/usuarios/{user_id}/bikes/{bike_id}", json=payload)
                if response.status_code == 201:
                    st.success("Empréstimo registrado com sucesso!")
                else:
                    st.error(response.json().get("error", "Erro ao registrar empréstimo."))

    st.markdown("---")

    # Sub-seção: Lista de Empréstimos
    st.subheader("Lista de Empréstimos")
    response = requests.get(f"{API_URL}/emprestimos")
    if response.status_code == 200:
        emprestimos = response.json()
        if emprestimos:
            for emp in emprestimos:
                st.write(f"**ID Empréstimo:** {emp.get('_id')}")
                st.write(f"**ID Usuário:** {emp.get('id_usuario')}")
                st.write(f"**ID Bicicleta:** {emp.get('id_bike')}")
                st.write(f"**Data de Aluguel:** {emp.get('data_aluguel')}")
                st.write("---")
        else:
            st.info("Nenhum empréstimo encontrado.")
    else:
        st.error(response.json().get("error", "Erro ao buscar empréstimos."))

    st.markdown("---")

    # Sub-seção: Deletar Empréstimo (Devolver Bicicleta)
    st.subheader("Devolver Bicicleta (Deletar Empréstimo)")
    with st.form(key='delete_loan_form'):
        delete_loan_id = st.text_input("ID do Empréstimo a Deletar")
        submit_delete_loan = st.form_submit_button("Deletar Empréstimo")

    if submit_delete_loan:
        if not delete_loan_id:
            st.error("O ID do empréstimo é obrigatório.")
        else:
            # Enviar um corpo JSON vazio ou com data_devolucao
            response = requests.delete(f"{API_URL}/emprestimos/{delete_loan_id}", json={})
            # Alternativamente, para enviar a data de devolução atual:
            # import datetime
            # data_devolucao = datetime.date.today().strftime("%Y-%m-%d")
            # payload = {"data_devolucao": data_devolucao}
            # response = requests.delete(f"{API_URL}/emprestimos/{delete_loan_id}", json=payload)

        if response.status_code == 200:
            st.success("Empréstimo deletado e bicicleta devolvida com sucesso!")
        else:
            # Tente obter mensagens de erro mais detalhadas, se disponíveis
            try:
                error_message = response.json().get("error", response.json().get("message", "Erro ao deletar empréstimo."))
            except:
                error_message = "Erro ao deletar empréstimo."
            st.error(error_message)

    st.markdown("---")

    # Sub-seção: Filtrar Empréstimos por Usuário
    st.subheader("Filtrar Empréstimos por Usuário")
    with st.form(key='filter_loans_user_form'):
        user_filter_id = st.text_input("ID do Usuário")
        submit_filter_user = st.form_submit_button("Filtrar")

    if submit_filter_user:
        if not user_filter_id:
            st.error("O ID do usuário é obrigatório.")
        else:
            response = requests.get(f"{API_URL}/emprestimos/usuarios/{user_filter_id}")
            if response.status_code == 200:
                user_loans = response.json()
                if user_loans:
                    for emp in user_loans:
                        st.write(f"**ID Empréstimo:** {emp.get('_id')}")
                        st.write(f"**ID Bicicleta:** {emp.get('id_bike')}")
                        st.write(f"**Data de Aluguel:** {emp.get('data_aluguel')}")
                        st.write("---")
                else:
                    st.info("Nenhum empréstimo encontrado para este usuário.")
            else:
                st.error(response.json().get("error", "Erro ao filtrar empréstimos."))

    st.markdown("---")

    # Sub-seção: Filtrar Empréstimos por Bicicleta
    st.subheader("Filtrar Empréstimos por Bicicleta")
    with st.form(key='filter_loans_bike_form'):
        bike_filter_id = st.text_input("ID da Bicicleta")
        submit_filter_bike = st.form_submit_button("Filtrar")

    if submit_filter_bike:
        if not bike_filter_id:
            st.error("O ID da bicicleta é obrigatório.")
        else:
            response = requests.get(f"{API_URL}/emprestimos/bikes/{bike_filter_id}")
            if response.status_code == 200:
                bike_loans = response.json()
                if bike_loans:
                    for emp in bike_loans:
                        st.write(f"**ID Empréstimo:** {emp.get('_id')}")
                        st.write(f"**ID Usuário:** {emp.get('id_usuario')}")
                        st.write(f"**Data de Aluguel:** {emp.get('data_aluguel')}")
                        st.write("---")
                else:
                    st.info("Nenhum empréstimo encontrado para esta bicicleta.")
            else:
                st.error(response.json().get("error", "Erro ao filtrar empréstimos."))
