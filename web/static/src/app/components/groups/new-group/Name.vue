<template>
	<div>
		<label class="mdc-text-field mdc-text-field--filled text-field--inner"
			   v-text-field>
			<input class="mdc-text-field__input" v-model="name">
			<span class="mdc-floating-label">Name</span>
			<span class="mdc-line-ripple" ref="ripple"></span>
		</label>
	</div>
</template>
<script>
	import { textField } from '../../../../directives.js'
	
	export default {
		name: 'Name',
		computed: {
			name: {
				get() {
					return this.$store.state.groups.newGroup.name
				},
				set(value) {
					this.$store.dispatch('groups/newGroup/setName', value, {root: true})
				}
			}
		},
		directives: {
			textField
		}
	}
</script>
<style scoped>
</style>
