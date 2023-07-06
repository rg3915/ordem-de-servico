const data = document.currentScript.dataset
const csrf = data.csrf

const getData = () => ({
  clientes: [],
  cliente: {},
  clienteSelecionado: {},
  searchCliente: '',
  servicos: [],
  servico: {},
  servicoSelecionado: {},
  searchServico: '',
  ordemServico: {},
  ordemServicoItem: {},
  currentId: 1,
  ordemServicoItems: [],
  clienteShow: false,
  servicoShow: false,

  init() {
    // watch - monitora as ações
    this.$watch('searchCliente', (newValue, oldValue) => {
      if (!newValue) this.clientes = []
      if (newValue.length >= 3) {
        this.getClientes(newValue)
      }
    })
    this.$watch('searchServico', (newValue, oldValue) => {
      if (!newValue) this.servicos = []
      if (newValue.length >= 3) {
        this.getServicos(newValue)
      }
    })
  },

  addItem() {
    // Envia os dados para inserir um novo item na Ordem de Serviço Item,
    // que por sua vez será retornado na tabela de itens.
    const servico_id = this.servicoSelecionado.id
    const servico_titulo = this.servicoSelecionado.titulo
    const valor = this.ordemServicoItem.valor
    const proxima_visita = this.ordemServicoItem.proximaVisita

    let ordem_servico_item_id = this.currentId++
    this.ordemServicoItems.push({ id: ordem_servico_item_id, servico_id, servico_titulo, valor, proxima_visita })
  },

  deleteOrdemServicoItem(id) {
    const indexToRemove = this.ordemServicoItems.findIndex(i => i.id == id)
    this.ordemServicoItems.splice(indexToRemove, 1)
  },

  getClientes(newValue) {
    const search = newValue
    fetch(`/api/v1/crm/cliente/?search=${search}`)
      .then(response => response.json())
      .then(data => {
        this.clientes = data
        this.clienteShow = true
      })
  },

  getCliente(cliente) {
    this.clienteSelecionado = cliente
    this.clienteShow = false
  },

  getServicos(newValue) {
    const search = newValue
    fetch(`/api/v1/servico/servico/?search=${search}`)
      .then(response => response.json())
      .then(data => {
        this.servicos = data
        this.servicoShow = true
      })
  },

  getServico(servico) {
    this.servicoSelecionado = servico
    this.servicoShow = false
  },

  saveData() {
    const cliente_id = this.clienteSelecionado.id
    const situacao = this.ordemServico.situacao
    const ordem_servico_itens = this.ordemServicoItems
    const bodyData = { cliente_id, situacao, ordem_servico_itens }
    fetch('/api/v1/servico/ordem-servico/', {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": csrf },
        body: JSON.stringify(bodyData),
      })
      .then(response => response.json())
      .then(data => {
        // redirect para os detalhes da OrdemServico
        const ordem_servico_id = data.ordem_servico_id
        window.location.href = `/servico/${ordem_servico_id}/`
      })
  },

})