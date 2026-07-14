from django.test import TestCase

# from datetime import date, timedelta
# from django.urls import reverse

# from .forms import UserCadastroForm
# from django.contrib.auth.models import User
# from .models import Historico, Livro, MinhaBiblioteca, PerfilUsuario

# class CadastroUsuarioFormTests(TestCase):
#     def form_data(self, **overrides):
#         data = {
#             'first_name': 'Maria',
#             'last_name': 'Silva',
#             'email': 'maria@example.com',
#             'username': 'maria',
#             'data_nascimento': '1990-01-01',
#             'cpf': '12345678901',
#             'telefone': '11999999999',
#             'password1': 'SenhaForte123',
#             'password2': 'SenhaForte123',
#         }
#         data.update(overrides)
#         return data

#     def test_form_cria_user_e_perfil(self):
#         form = UserCadastroForm(data=self.form_data())

#         self.assertTrue(form.is_valid(), form.errors)
#         user = form.save()

#         self.assertEqual(user.email, 'maria@example.com')
#         self.assertTrue(PerfilUsuario.objects.filter(usuario=user).exists())

#     def test_form_rejeita_email_e_cpf_duplicados(self):
#         user = User.objects.create_user(
#             username='maria',
#             email='maria@example.com',
#             password='SenhaForte123'
#         )
#         PerfilUsuario.objects.create(
#             usuario=user,
#             data_nascimento=date(1990, 1, 1),
#             cpf='12345678901',
#             telefone='11999999999'
#         )

#         form = UserCadastroForm(data=self.form_data(username='outra'))

#         self.assertFalse(form.is_valid())
#         self.assertIn('email', form.errors)
#         self.assertIn('cpf', form.errors)

#     def test_form_rejeita_data_futura(self):
#         amanha = date.today() + timedelta(days=1)
#         form = UserCadastroForm(
#             data=self.form_data(data_nascimento=amanha.isoformat())
#         )

#         self.assertFalse(form.is_valid())
#         self.assertIn('data_nascimento', form.errors)

#     def test_view_cadastro_cria_usuario_e_redireciona_para_login(self):
#         response = self.client.post(
#             reverse('formulario_cadastro'),
#             data=self.form_data()
#         )

#         self.assertRedirects(response, reverse('login'))
#         self.assertTrue(User.objects.filter(username='maria').exists())
#         self.assertTrue(
#             PerfilUsuario.objects.filter(cpf='12345678901').exists()
#         )


# class AutenticacaoUsuarioTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='joao',
#             email='joao@example.com',
#             password='SenhaForte123'
#         )

#     def test_login_por_email(self):
#         response = self.client.post(reverse('verificar_login'), {
#             'email': 'joao@example.com',
#             'senha': 'SenhaForte123',
#         })

#         self.assertRedirects(response, reverse('acesso_painel'))

#     def test_usuario_logado_nao_acessa_login_ou_cadastro(self):
#         self.client.force_login(self.user)

#         login_response = self.client.get(reverse('login'))
#         cadastro_response = self.client.get(reverse('formulario_cadastro'))

#         self.assertRedirects(login_response, reverse('acesso_painel'))
#         self.assertRedirects(cadastro_response, reverse('acesso_painel'))

#     def test_painel_exige_usuario_autenticado(self):
#         response = self.client.get(reverse('acesso_painel'))

#         self.assertRedirects(
#             response,
#             f"{reverse('login')}?next={reverse('acesso_painel')}"
#         )


# class BibliotecaUsuarioTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='ana',
#             email='ana@example.com',
#             password='SenhaForte123'
#         )
#         self.outro_user = User.objects.create_user(
#             username='carlos',
#             email='carlos@example.com',
#             password='SenhaForte123'
#         )
#         self.livro = Livro.objects.create(
#             nome='Livro Teste',
#             descricao='Descricao',
#             autor='Autor',
#             genero='Ficcao',
#             editora='Editora',
#             pagina_livro=120,
#             livro_imagem='home/images/livros/livro-1.jpg',
#             ordem=1,
#             **{'data_publica\u00e7\u00e3o': date(2020, 1, 1)}
#         )

#     def test_adicionar_livro_salva_usuario_e_historico(self):
#         self.client.force_login(self.user)

#         response = self.client.get(
#             reverse('adicionar_biblioteca', args=[self.livro.id])
#         )

#         self.assertRedirects(response, reverse('biblioteca_pessoal'))
#         self.assertTrue(
#             MinhaBiblioteca.objects.filter(
#                 usuario=self.user,
#                 id_livro=self.livro
#             ).exists()
#         )
#         self.assertTrue(
#             Historico.objects.filter(
#                 usuario=self.user,
#                 nome_livro=self.livro.nome
#             ).exists()
#         )

#     def test_biblioteca_filtra_por_usuario_logado(self):
#         MinhaBiblioteca.objects.create(
#             usuario=self.outro_user,
#             id_livro=self.livro,
#             nome=self.livro.nome,
#             imagem_capa=self.livro.livro_imagem
#         )
#         self.client.force_login(self.user)

#         response = self.client.get(reverse('biblioteca_pessoal'))

#         self.assertEqual(list(response.context['dados']), [])

#     def test_rota_legada_bilioteca_continua_funcionando(self):
#         self.client.force_login(self.user)

#         response = self.client.get(reverse('biblioteca_pessoal_legado'))

#         self.assertEqual(response.status_code, 200)

#     def test_usuario_nao_remove_livro_de_outro_usuario(self):
#         item = MinhaBiblioteca.objects.create(
#             usuario=self.outro_user,
#             id_livro=self.livro,
#             nome=self.livro.nome,
#             imagem_capa=self.livro.livro_imagem
#         )
#         self.client.force_login(self.user)

#         response = self.client.post(reverse('remover_livro', args=[item.id]))

#         self.assertEqual(response.status_code, 404)
#         self.assertTrue(MinhaBiblioteca.objects.filter(id=item.id).exists())
